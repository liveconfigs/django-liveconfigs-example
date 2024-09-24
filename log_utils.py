import json
import logging


_OMIT = {'__dict__', '__class__', '__dir__', 'levelno', 'levelname',
         'exc_info', 'stack_info', 'request', 'msg', 'args', 'message'}


class JsonFormatter(logging.Formatter):
    """ slightly more usable than json-log-formatter """

    def __init__(self):
        super().__init__()

    def format(self, record):
        """ copy & paste from standard logger """
        message = record.getMessage()
        data = {
            'message': message,
            'level': record.levelname,
            'severity': record.levelname,
            'timestamp': record.created,
            'timestamp_str': str(record.created)
        }
        if record.exc_info:
            record.exc_text = self.formatException(record.exc_info)
        if record.stack_info:
            data['stack_info'] = self.formatStack(record.stack_info)
        for attr, value in record.__dict__.items():
            if attr not in _OMIT:
                data[attr] = value

        return json.dumps(data, default=str)
