int InNum = 5;
int HidNum = 15;
int OutNum = 5;

float TotalError;

float[] In = new float [InNum];
float[] Hid = new float [HidNum];
float[] HidError = new float [HidNum];
float[] Out = new float  [OutNum];
float[] OutError = new float  [OutNum];
float[] OutGoal = new float  [OutNum];

float [] HidSyn = new float [InNum * HidNum];
float [] HidSynError = new float [InNum * HidNum];

float [] OutSyn = new float [OutNum * HidNum];
float [] OutSynError = new float [OutNum * HidNum];

color pink = color(255, 0, 136);
color blue = color(30, 201, 227);
color green = color(0, 255, 44);
color white = color(225, 225, 225);

void setup(){
  size(500, 500);

  for(int i = 0; i < InNum; i++)
  {
    In[i] = random (10);
  }
  
  for(int o = 0; o < OutNum; o++)
  {
    OutGoal[o] = random (10);
  }
  
  for(int hs = 0; hs < InNum * HidNum; hs++)
  {
    HidSyn [hs] = random (-5, 5);
  }
  
  for(int os = 0; os < HidNum * OutNum; os++)
  {
    OutSyn[os] = random (-5, 5);
  }
}

void draw ()
{
  background(75);
  
  Input();
  
  Hidden();
  
  Output();
  
  Training();
  
  GUI();
}

void Input()
{
  for(int i = 0; i < InNum; i++)
  {
    noStroke ();
    fill (lerpColor(blue, pink, In [i] * 0.08));
    rect (0, i*20, 20, 20);
  }
}

void Hidden()
{
  for(int h = 0; h < HidNum; h++)
  {
    for(int i = 0; i < InNum; i++)
    {
      Hid [h] += (In [i] * HidSyn [i + h * InNum]) / HidNum;
      stroke (lerpColor(white, green, HidSyn [i + h * InNum] * 0.08));
      line ((width-40)/2, h * 20 + 10, 20, i*20 + 10);
    }
    Hid [h] = (Hid [h] + abs (Hid [h]))/2;
    
    noStroke ();
    fill (lerpColor(blue, pink, Hid[h] * 0.08));
    rect((width-40)/2,  h*20, 20, 20);
  }
}

void Output()
{
  for(int o = 0; o < OutNum; o++)
  {
    for(int h = 0; h < HidNum; h++)
    {
      Out[o] += Hid [h] * OutSyn [h + o * HidNum];
      stroke (lerpColor(white, green, OutSyn [h + o * HidNum] * 0.08));
      line((width-40)/2 + 20, h * 20 + 10, width - 40, o * 20 + 10);
    }
    Out [o] = Out [o] / OutNum;
    Out [o] = (Out [o] + abs (Out [o])) / 2;
    
    noStroke ();
    fill (lerpColor(blue, pink, Out[o] * 0.08));
    rect(width-40,  o*20, 20, 20);
    fill (lerpColor(blue, pink, OutGoal[o] * 0.08));
    rect(width-20,  o*20, 20, 20);
  }
}

void Training()
{
  for(int o = 0; o < OutNum; o++)
  {
    OutError [o] = OutGoal [o] - Out [o];
    TotalError += OutError [o];
    for(int h = 0; h < HidNum; h++)
    {
      HidError [h] += OutError [o] * OutSyn [h + o * HidNum];
      
      OutSynError [h + o * HidNum] = OutError [o] - (OutSyn [h + o * HidNum] * Hid [h]) / HidNum;
      OutSyn [h + o * HidNum] += OutSynError [h + o * HidNum] * 0.005;
    }
    Out [o] = 0;
  }
  
  for(int h = 0; h < HidNum; h++)
  {
    for(int i = 0; i < InNum; i++)
    {
      HidSynError [i + h * InNum] = HidError [h] * In[i];
      HidSyn [i + h * InNum] += HidSynError [i + h * InNum] * 0.005;
    }
    Hid [h] = 0;
    HidError [h] = 0;
  }
}

void GUI()
{
   strokeWeight(4);
  stroke(green);
  fill(235);
  rect(2, height - height/5, width - 3, height/5 - 4);
  strokeWeight(1);
  
  fill(0);
  textSize(20);
  text("Total Error:", width / 12, height - height/4 + (height/5) / 2);
  text(TotalError, width / 12 - 6, height - height/5 + (height/5) / 2);
  TotalError = 0;
}