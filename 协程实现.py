import asyncio
async def request(url):
    print('正在请求%s的实现'%url)
    print('请求成功')

a=request('www.baidu.com')

#创建一个事件循环对象
loop=asyncio.get_event_loop()

#将协程对象注册到事件循环对象loop中，启动loop
loop.run_until_complete(a)