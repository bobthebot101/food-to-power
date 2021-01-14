
kj = float(input('How much KJ have you had Today (Just the Number): '))

wh = (kj/3.6)

ps4pro = (wh/310)
ps4slim = (wh/165)
xbox1x = (wh/180)
iphone12promax = (wh/14.13)
iphone12andpro = (wh/10.78)
hp = (wh/746)
kwh = (wh/1000)

print(f'With {kj}kj you can:')
print(f'    Charge a iPhone 12 Pro Max {iphone12promax} Times')
print(f'    Charge a iPhone 12/Pro {iphone12andpro} Times')
print(f'    Play for {ps4pro} Hours on a Ps4 Pro')
print(f'    Play for {ps4slim} Hours on a Ps4 slim')
print(f'    Play for {xbox1x} Hours on a Xbox One X')
print(f'    {kj}kj = {wh}wh')
print(f'    Thats {kwh} kwh !!')
print(f'    Thats {hp} Horsepower')
