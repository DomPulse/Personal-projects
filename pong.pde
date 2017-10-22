PFont font;
PVector Ball = new PVector();
PVector Vel = PVector.random2D();
PVector score = new PVector();
float LP;
float RP;

void setup(){
 size(700, 700);
 font = loadFont("Consolas-Bold-32.vlw");
 LP = height/2;
 RP = height/2;
 reset();
 stroke(255);
 strokeWeight(20);
 rectMode(CENTER);
}

void draw(){
 background(0);
 
 rect(width/2, 20, width, 10);
 rect(width/2, height-20, width, 10);
 
 for(int i = 50; i < height-30; i+=40){
   rect(width/2, i, 2.5, 2.5);
 }
 
 score();
 paddle();
 move();
 point(Ball.x, Ball.y);
}

void score(){
  if(Ball.x >= width){
    score.x++;
    reset();
  }
  else if(Ball.x <= 0){
    score.y++;
    reset();
  }
  textFont(font, 50);
  text(int(score.x), width/2-150, 100);
  text(int(score.y), width/2+150, 100);
}

void reset(){
  Ball.x = width/2;
  Ball.y = height/2;
  LP = height/2;
  RP = height/2;
  Vel.x = 7;
  Vel.y = 0;
}

void move(){
  Ball.x += Vel.x;
  Ball.y += Vel.y;
  bounce();
}

void bounce(){
  if(Ball.y <= 30){
    Vel.y = -Vel.y;
  }
  if(Ball.y >= height-30){
    Vel.y = -Vel.y;
  }
  
  if(Ball.x >= width-45 && abs(RP-Ball.y) <= 70){
    Vel.x = -Vel.x;
    Vel.y -= (RP-Ball.y)/7;
  }
  if(Ball.x <= 45 && abs(LP-Ball.y) <= 70){
    Vel.x = -Vel.x;
    Vel.y -= (LP-Ball.y)/7;
  }
}

void paddle(){
  rect(30, LP, 5, 125);
  rect(width-30, RP, 5, 125);
  if(key == 'w' && keyPressed && LP >= 115)
  LP-=5;
  if(key == 's' && keyPressed && LP <= height-115)
  LP+=5;
  
  if(Ball.y < RP && RP >= 115)
  RP-=5;
  if(Ball.y > RP && RP <= height-115)
  RP+=5;  
}