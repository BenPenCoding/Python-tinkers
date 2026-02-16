#Imports
import turtle
import random
import RadarGraphics

#Classes

#Enemy is the class that represents all enemies in the game.

#Speed and aggression control the enemy's behavior. Speed is the number of pixels the enemy travels /s.
#Aggression (0,1] governs the movement direction, an aggression closer to 1 will mean the enemy is more 
#likely to move straight towards the centre. Closer to 0, its movement will be much more random. 
#x and y represent the coordinates of the enemy. 
class Enemy():

    def __init__(self, speed, aggression, angle, distance):

        self.speed = speed
        self.aggression = aggression
        self.angle = angle 
        self.distance = distance
        
        self.scansSinceLastScan = 0
        self.scanned = False
        self.colour = 'Red'
        self.scannedColour = 'Green'

    def getAngle(self):

        return self.angle

    def setAngle(self, newAngle):

        self.angle = newAngle

    def getDistance(self):

        return self.distance

    def setDistance(self, newDistance):

        self.distance = newDistance

    def getSpeed(self):

        return self.speed

    def getAggression(self):

        return self.aggression

    def getColour(self):

        return self.colour

    def getScannedColour(self):

        return self.scannedColour

    def resetScansSinceLastScan(self):

        self.scansSinceLastScan = 0

    def addScansSinceLastScan(self):

        self.scansSinceLastScan += 1

    def getScansSinceLastScan(self):

        return self.scansSinceLastScan

    def isScanned(self):

        return True if self.scanned else False

    def scan(self):

        self.scanned = True
        self.resetScansSinceLastScan()

    def unscan(self):

        self.scanned = False
            

#Radar is the class that represents the radar in the centre of the game. 

#Turn speed is the degrees /s that the radar will turn. Range is the number of pixels the radar can reach.
#Size is how large the radar itself is. This acts as a way to change how close an enemy needs to be to end
#the game. 
class Radar():

    def __init__(self, turnSpeed, size):

        self.turnSpeed = turnSpeed
        self.size = size

        self.angle = 0

    def getAngle(self):

        return self.angle

    def getSize(self):

        return self.size

    def incrementAngle(self):

        self.angle = (self.angle + 1) % 360


#Functions

#spawnEnemies spawns enemies around the area.

#numEnemies is the number of enemies to be spawned, minDistance is the minimum distance from the centre that
#enemies can spawn, maxDistance is the maximum distance from the centre that enemies can spawn, and finally
#enemyClass
def spawnEnemies(numEnemies, minDistance, maxDistance, enemyClass):

    enemies = []

    for i in range(numEnemies):

        angle = random.randint(0,359)

        distance = random.randint(minDistance, maxDistance)
        
        enemies.append(enemyClass(10, 0.5, angle, distance))

    return enemies

def moveEnemy(enemy):

    angle = enemy.getAngle()
    distance = enemy.getDistance()
    speed = enemy.getSpeed()

    angleChange = random.randint(-speed, speed)
    angle += angleChange

    displacement = random.randint(-speed, speed)

    if distance + displacement > 50 and distance + displacement < 300:

        distance += displacement

    enemy.setAngle(angle)
    enemy.setDistance(distance)

def scanForEnemies(enemies, radar):

    scanAngle = radar.getAngle()

    for enemy in enemies:

        if enemy.getAngle() == scanAngle:

            enemy.scan()
            enemy.resetScansSinceLastScan()

        else:

            enemy.addScansSinceLastScan()

        if enemy.getScansSinceLastScan() >= 90:

            enemy.unscan()
            moveEnemy(enemy)


#Main

tt = turtle.Turtle()
tt.hideturtle()
tt.speed(0)

centreRadar = Radar(30, 50)

enemies = spawnEnemies(40, 200, 300, Enemy)

RadarGraphics.drawStillFrame(enemies, tt)

while True:

    #Draw
    turtle.tracer(0)
    RadarGraphics.drawFrame(enemies, centreRadar, tt)
    turtle.update()

    #Modify attriubutes
    scanForEnemies(enemies, centreRadar)
    centreRadar.incrementAngle()

    #Reset frame
    tt.clear()





