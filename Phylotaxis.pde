//http://algorithmicbotany.org/papers/abop/abop-ch4.pdf this thing helps alot
int n;
float a = 137.5; // vary this to make differenct patterns
float r;
float p;
float c;
void setup(){
  size(400, 400);
  background(0);
  strokeWeight(5);
  colorMode(HSB);
}
void draw(){
  translate(width/2, height/2);
  p = n*a;
  r = 5*sqrt(n);
  c = map(n, 0, 600, 0, 255);
  if(n < 600)
  n++;
  stroke(c, 255, 255);
  point(r * sin(p), r * cos(p));
}