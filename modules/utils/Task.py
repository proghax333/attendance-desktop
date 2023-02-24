
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread, QObject, QRunnable, QThreadPool

class Worker(QObject):
    finished = pyqtSignal(object)
    # progress = pyqtSignal(int)

    def __init__(self, **kwargs) -> None:
      super().__init__(**kwargs)
      self.task = lambda: None

    def set_task(self, task):
      self.task = task
    
    def get_task(self):
      return self.task

    def run(self):
      result = self.task()
      self.finished.emit(result)

class AsyncTask(QObject):
  finished = pyqtSignal(object)

  def __init__(self, task, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.task = task

    self.thread = QThread()
    
    self.worker = Worker()
    self.worker.set_task(self.task)
    self.worker.moveToThread(self.thread)

    self.thread.started.connect(self.worker.run)
    self.worker.finished.connect(self.finished)
    self.worker.finished.connect(self.thread.quit)
    self.worker.finished.connect(self.worker.deleteLater)
    self.thread.finished.connect(self.thread.deleteLater)
  
  def start(self):
    return self.thread.start()
