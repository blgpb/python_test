class Person(object):
    '''定义一个类 人'''
    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name
        self.gun = None#用来保存枪对象的引用
        self.hp = 100#剩余的血量
    def anzhuang_zidan(self,dan_jia_temp, zi_dan_temp):
        '''把子弹装到弹夹中'''
        #弹夹保存子弹
        dan_jia_temp.baocun_zidan(zi_dan_temp)
    def anzhuang_danjia(self, gun_temp, dan_jia_temp):
        '''把弹夹安装到枪中'''
        #枪保存弹夹
        gun_temp.baocun_danjia(dan_jia_temp)
    def naqiang(self, gun_temp):
        '''老王拿起一把枪'''
        self.gun = gun_temp
    def __str__(self):
        if self.gun:
            return '%s的血量为:%d;他有枪;%s'%(self.name, self.hp, self.gun)
        else:
            if self.hp > 0:
                return '%s的血量为:%d;他没有枪'%(self.name, self.hp)
            else:
                return '敌人已死'
    def kou_ban_ji(self, di_ren):
        '''让枪发射子弹打敌人'''
        #枪.开火（敌人）
        self.gun.fire(di_ren)
    def diao_xue(self, sha_shang_li):
        '''根据杀伤力，人掉相应的血'''
        self.hp -= sha_shang_li

class Gun(object):
    '''枪类'''
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name#用来记录枪的类型
        self.danjia = None#用来记录弹夹对象的引用
    def baocun_danjia(self, dan_jia_temp):
        '''用一个属性来保存这个弹夹对象的引用'''
        self.danjia = dan_jia_temp
    def __str__(self):
        if self.danjia:
            return '枪的信息为:%s, %s' % (self.name, self.danjia)
        else:
            return '枪的信息为:%s,这把枪中没有弹夹'%(self.name)
    def fire(self, di_ren):
        '''枪从弹夹中获取一发子弹，然后让这发子弹去击中敌人'''
        #先从弹夹中弹出子弹
        #弹夹.弹出一发子弹
        zidan_fire = self.danjia.tanchu_zidan()
        #让这个子弹去伤害敌人
        if zidan_fire:
            #子弹.打中敌人(敌人)
            zidan_fire.dazhong(di_ren)
        else:
            print('弹夹中没有子弹了')
class Danjia(object):
    def __init__(self, max_num):
        super(Danjia, self).__init__()
        self.max_num = max_num#用来记录弹夹最大装子弹的个数
        self.zidan_list = []#用来记录所有子弹的引用
    def baocun_zidan(self, zi_dan_temp):
        '''将这颗子弹保存. 保存的是 子弹的实例对象'''
        if zi_dan_temp not in self.zidan_list:#如果弹夹中已经有了这发子弹，就不能重新安装这发子弹
            self.zidan_list.append(zi_dan_temp)
    def __str__(self):
        return '弹夹的信息为：%d/%d'%(len(self.zidan_list), self.max_num)
    def tanchu_zidan(self):
        '''弹出最上面的那颗子弹'''
        if self.zidan_list:
            return self.zidan_list.pop()
        else:
            return None
class Zidan(object):
    def __init__(self, sha_shang_li):
        super(Zidan, self).__init__()
        self.sha_shang_li = sha_shang_li#一颗子弹的伤害
    def dazhong(self, di_ren):
        '''让敌人掉血'''
        #敌人.掉血(一颗子弹的伤害)
        di_ren.diao_xue(self.sha_shang_li)
def main():
    #1. 创建老王对象
    laowang = Person('老王')
    #2. 创建一个枪对象
    ak47 = Gun('AK47')
    #3. 创建一个弹夹对象(弹夹最多能装20发子弹)
    dan_jia = Danjia(20)
    #4. 创建一发子弹（子弹的伤害力为10）
    #每发子弹的名字（类似于子弹的编号）都是独一无二的，不能重复
    zi_dan = Zidan(10)
    Super_zi_dan = Zidan(30)
    #5. 老王把子弹安装到弹夹中（弹夹，子弹）
    laowang.anzhuang_zidan(dan_jia, zi_dan)
    laowang.anzhuang_zidan(dan_jia, Super_zi_dan)
    #6. 老王把弹夹安装到枪中（枪，弹夹）
    laowang.anzhuang_danjia(ak47, dan_jia)
    #test:测试弹夹的信息
    #print(dan_jia)
    #test:测试枪的信息
    #print(ak47)
    #7. 老王拿枪
    laowang.naqiang(ak47)
    #test:测试老王对象
    print(laowang)
    #8. 创建一个敌人
    gebi_laosong = Person('隔壁老宋')
    print(gebi_laosong)
    #9.老王开枪打敌人(老王扣扳机)
    laowang.kou_ban_ji(gebi_laosong)
    print(laowang)
    print(gebi_laosong)

if __name__ == '__main__':
    main()