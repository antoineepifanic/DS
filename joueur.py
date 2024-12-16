class Player:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 300
        self.y = 300  
        self.size = 30  
        self.speed = 5  

        self.shape = self.canvas.create_rectangle(
            self.x - self.size/2,  # x1
            self.y - self.size/2,  # y1
            self.x + self.size/2,  # x2
            self.y + self.size/2,  # y2
            fill='red'
        )

        self.canvas.bind_all('<Left>', self.move_left)
        self.canvas.bind_all('<Right>', self.move_right)
        self.canvas.bind_all('<Up>', self.move_up)
        self.canvas.bind_all('<Down>', self.move_down)

    def move_left(self, event):
        self.canvas.move(self.shape, -self.speed, 0)
        
    def move_right(self, event):
        self.canvas.move(self.shape, self.speed, 0)
        
    def move_up(self, event):
        self.canvas.move(self.shape, 0, -self.speed)
        
    def move_down(self, event):
        self.canvas.move(self.shape, 0, self.speed)