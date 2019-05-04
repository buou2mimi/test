# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/3 16:40
# 文件名称：test1.py
# 开发软件：PyCharm
def site(city,country,population = ''):
    city = city
    country = country
    population = population
    if population:
        specific_location = city.title() + ',' + country.title() + ' -population ' + str(population)
    else:
        specific_location = city.title() + ',' + country.title()
    return specific_location