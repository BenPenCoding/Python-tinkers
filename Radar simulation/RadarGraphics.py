#Functions

def drawFrame(enemies, radar, turt):

    drawEnemies(turt, enemies, 20, True)
    drawRadar(turt, radar)

def drawRadar(turt, radar):

    turt.penup()
    turt.home()

    turt.color("gray")

    turt.pendown()
    turt.dot(radar.getSize())

    turt.penup()
    turt.home()

    turt.right(radar.getAngle())

    turt.pendown()

    turt.pensize(5)

    turt.forward(500)

def drawEnemy(enemy, turt, drawSize):

    turt.penup()
    turt.home()

    turt.right(enemy.getAngle())
    turt.forward(enemy.getDistance())

    turt.pendown()

    if enemy.isScanned():

        turt.color(enemy.getScannedColour())

    else:

        turt.color(enemy.getColour())

    turt.dot(drawSize)



def drawEnemies(turt, enemies, drawSize, onlyScanned = True):

    for enemy in enemies:

        if onlyScanned and enemy.isScanned():        

            drawEnemy(enemy, turt, drawSize)

        elif onlyScanned and not enemy.isScanned():

            pass

        else:

            drawEnemy(enemy, turt, drawSize)


