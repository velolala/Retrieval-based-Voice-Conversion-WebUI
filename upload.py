import gradio as gr
import shutil
import os
from pathlib import Path
import logging

log = logging.getLogger(__name__)


def upload_file(file):
  folder = "./data/upload/"
  if not os.path.exists(folder):
    os.mkdir(folder)
  shutil.copy(file.name, folder)
  name = Path(file.name).name
  log.info(f"uploaded file {name}")
  uploaded = Path(os.path.join(folder, name))
  log.info(uploaded.exists())
  return str(uploaded)
