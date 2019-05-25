FROM python:3
COPY . /
RUN pip install pynput
CMD ["python", "./RomRoamer.py"]
