int d = 10; //the size of ech slash
int x;
int y;

void setup()
{
  colorMode(HSB, width);
  size(600, 600);
  background(width/2);
}

void draw()
{
  stroke(x, width/2, width);
  strokeWeight(6);
  
  if(random(1) >= 0.5) //probability
  line(x, y, x + d, y + d); //backslash
    
  else
  line(x + d, y, x, y + d); //forward slash
    
  x+=d; //iterate x
  
  if(x % width == 0) //iterate y
  {
    x=0;
    y+=d;
  }
}