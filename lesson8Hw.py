進貨=1
出貨=2
營業額統計=3
庫存統計=4
離開系統=5
次=0
進=0
出=0
出口=0
x=0
收=0
收進=0
剩=0
print('請先設定')
最初=int(input('最初有幾顆蘋果:'))
幾元=int(input('一顆幾元:'))
print('進貨 1')
print('出貨 2')
print('營業額統計 3')
print('庫存統計 4')
print('離開系統 5')
x=int(input('請選擇功能:'))
while 0<x<5:
    print('---------------')
    if x==1:
        進=int(input('進幾顆蘋果:'))
        print('---------------')
    if x==2:
        剩=(最初+進)-出
        if 剩<出:
            print('庫存不足，請進貨')
        else:
            出口=int(input('賣出多少顆蘋果:'))
            出=出+出口
            收進=(出口*幾元)
            print('應收',收進,'元')
            print('---------------')
        次=次+1
        收=收+收進
        收進=0
        出口=0
    if x==3:
        print('今天有',次,'筆交易')
        print('賣出',出,'顆蘋果')
        print('共收',收,'元')
        print('---------------')
    if x==4:
        剩=(最初+進)-出
        print('剩:',剩,'顆蘋果')
        print('---------------')
    print('進貨 1')
    print('出貨 2')
    print('營業額統計 3')
    print('庫存統計 4')
    print('離開系統 5')
    x=int(input('請選擇功能:'))
