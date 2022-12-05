using System;
using System.Numerics;
using Raylib_cs;

namespace Client
{
    public class Bacteria
    {
        // screen size
        private int screenWidth;
        private int screenHeight;

        // ball properties
        private float posx;
        private float posy;
        private int radius = 5;
        private int updateFactor;
        public Vector2 position;


        private int prevCount = 0;
        private Body body;

        // constructor
        public Bacteria(int screenWidth, int screenHeight, int updateFactor, Body body)
        {
            // set screenHeight
            this.screenWidth = screenWidth;
            this.screenHeight = screenHeight;

            this.updateFactor = updateFactor;

            this.body = body;

            posx = (float)screenWidth / 2 + 20;
            posy = (float)screenHeight / 2 + 20;
        }

        public void deductHealth(int framesCounter)
        {
            if (framesCounter - this.prevCount < 60)
            {
                return;
            }
            this.body.updateHealth(1);
            this.prevCount = framesCounter;
            
        }

        public Vector2 getPosition()
        {
            return position;
        }

        public void updatePosition()
        {
            // get probs for updating
            Random rnd = new Random();
            int probx = rnd.Next(0, 101);
            int proby = rnd.Next(0, 101);

            if ((posx + updateFactor) <= screenWidth - radius && probx <= 50)
            {
                posx += updateFactor;
            }
            else if (posx - updateFactor >= radius)
            {
                posx -= updateFactor;
            }
            // y up or down
            if ((posy + updateFactor) <= screenHeight - radius && proby <= 50)
            {
                posy += updateFactor;
            }
            else if (posy - updateFactor >= radius)
            {
                posy -= updateFactor;
            }

            position.X = posx;
            position.Y = posy;
        }

        public void draw()
        {
            Raylib.DrawCircleV(position, radius, Color.GREEN);
        }



    }
}
