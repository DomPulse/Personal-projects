float[] sx = new float[1000];
float[] sy = new float[1000];
float fx;
float fy;
boolean w, a, s, d;
boolean alive = true;
int len = 1;
int MemD;

void setup()
{
  colorMode(HSB, 360, 100, 100);
  size(400, 400);
  sx[0] = 100;
  sy[0] = height/2 - 25;
  fx = 200;
  fy = height/2 - 25;
  
  for(int i = 1; i < len; i++)
  {
    sx[i] = -25;
    sy[i] = -25;
  }
}

void draw()
{
  frameRate(12);
  background(0, 0, 99);
  stroke(0, 99, 2);
  for(int x = 0; x < width; x += 25)
  {
    line(x, 0, x, height);
  }
  for(int y = 0; y < height; y += 25)
  {
    line(0, y, width, y);
  }

  fill(359, 99, 99);
  rect(fx, fy, 25, 25);
  
  eat();
  body();
  if(alive == true)
  move();
  else
  reset(); 
  die();
  fill(160, 81, 82);
  rect(sx[0], sy[0], 25, 25);
}

void body()
{
  int i = len;
  while (i > 0)
  {
    sx[i] = sx[i-1];
    sy[i] = sy[i-1];
    fill(160+((i+1)*2), 81, 82);
    rect(sx[i], sy[i], 25, 25);
    i--;
  }

}

void move()
{
  keyPressed();

  if(w == true)
  sy[0] -= 25;
  
  if(a == true)
  sx[0] -= 25;
  
  if(s == true)
  sy[0] += 25;
  
  if(d == true)
  sx[0] += 25;
  
}

void keyPressed()
{
  if(key != 'w' && key != 'a' && key != 's' && key != 'd')
  {
    if(w == true)
    key = 'w';
    
    if(a == true)
    key = 'a';
    
    if(s == true)
    key = 's';
    
    if(d == true)
    key = 'd';
  }
  
  if(key == 'w')
  w = true;
  else
  w = false;
  
  if(key == 'a')
  a = true;
  else
  a = false;
  
  if(key == 's')
  s = true;
  else
  s = false;
  
  if(key == 'd')
  d = true;
  else
  d = false;
  
}

void die()
{
  if(sx[0] >= width || sx[0] < 0 || sy[0] >= height || sy[0] < 0)
  {
    alive = false;
  }
  
  for(int i = 1; i < len; i++)
  {
    if(sx[0] == sx[i] && sy[0] == sy[i])
    {
      alive = false;
    }
  }
}

void reset()
{
    sx[0] = 100;
    sy[0] = height/2 - 25; 
    fx = 200;
    fy = height/2 - 25;
    alive = true;
    w = false;
    a = false;
    s = false;
    d = false;
    len = 1;
    key = 'k';
}

void newfood()
{
  fx = 25 * int(random(width/25));
  fy = 25 * int(random(height/25));
  for(int i = 0; i < len; i++)
  {
    if(sx[i] == fx && sy[i] == fy)
    newfood();
  }
}

void eat()
{
  if(sx[0] == fx && sy[0] == fy)
  {
    len++;
    newfood();
  }
}
