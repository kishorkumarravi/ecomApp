import logging

from .serializers import RegistrationSerializer, ItemsSerializer, OrderHistorySerializer

def create_user(record):
    try:
        logging.info(f'record.. {record}')
        tran_serializer = RegistrationSerializer(data=record)
        if tran_serializer.is_valid():
            tran_serializer.save()
            logging.info('Saved..')
            return True
        return False
            
    except Exception as err:
        logging.info(f'err.. {err}')
        return False

def create_items(record):
    try:
        logging.info(f'record.. {record}')
        tran_serializer = ItemsSerializer(data=record)
        if tran_serializer.is_valid():
            tran_serializer.save()
            logging.info('Saved..')
            return True
        return False
            
    except Exception as err:
        logging.info(f'err.. {err}')
        return False

def create_history(record):
    try:
        logging.info(f'record.. {record}')
        tran_serializer = OrderHistorySerializer(data=record)
        if tran_serializer.is_valid():
            tran_serializer.save()
            logging.info('Saved..')
            return True
        return False
            
    except Exception as err:
        logging.info(f'err.. {err}')
        return False