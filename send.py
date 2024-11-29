import time
import asyncio
import aiohttp



async def async_send(idx, url, session: aiohttp.ClientSession):
    try:
        print('отправка запроса', idx)
        async with session.get(url) as response:
            if 200 <= response.status < 300:
                text = 'успешно'
            else:
                text = 'безуспешно'
            print(f'{idx} | {url}: {text}', end='\n')
    except Exception as e:
        print('error', e ,idx)

async def async_run(count):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(count):
            time.sleep(0.01)
            #await asyncio.sleep(0.01)
            tasks.append(async_send(idx=i, url='http://127.0.0.1:8000', session=session))
        await asyncio.gather(*tasks)

def async_main():
    asyncio.run(async_run(100))

async_main()


######################################


# class Objects:
#     data = {
#     1: {"to_user": "recipient1", "from_user": "sender1", "message": "Hello, how are you?"},
#     2: {"to_user": "recipient2", "from_user": "sender2", "message": "Meeting at 5 PM."},
#     3: {"to_user": "recipient3", "from_user": "sender3", "message": "Happy Birthday!"},
#     4: {"to_user": "recipient4", "from_user": "sender4", "message": "Can you send the report?"},
#     5: {"to_user": "recipient5", "from_user": "sender5", "message": "Let's catch up soon."}
# }
#
#     def get(self,pk=None):
#         if pk is None:
#             raise TypeError
#         return MyModel(pk = pk)
#
# class MyModelMeta(type):
#     def create_local_attrs(self,*args,**kwargs):
#         if 'pk' in kwargs.keys():
#             pk = kwargs['pk']
#             database_data =  self.objects.data[pk] #имитируем запрос в базу данных
#             for key, value in database_data.items():
#                 if key in self.__class_attrs:
#                     self.__dict__[key] = value
#
#
#
#     def __init__(cls, name, bases, attrs):
#         super().__init__(name, bases, attrs) #по факту не надо
#         cls.objects = Objects() #создаем вложенный экземпляр класса
#         cls.__class_attrs = {key for key in attrs.keys() if not key.startswith("__")} #сет из нужных атрибутов класса
#         cls.__init__ = MyModelMeta.create_local_attrs #создаем новый инит для класса
#
#     def __call__(cls, *args, **kwargs):
#         return super().__call__(*args, **kwargs) #создает обтект,вызывает его new & init
#
# class MyModel(metaclass=MyModelMeta):
#     from_user = 'charfield'
#     to_user = 'charfield'
#
#
# mail = MyModel.objects.get(pk=2)
#
#
# print(mail.__dict__)
# print(mail.from_user)
# print(mail.to_user)


























#
