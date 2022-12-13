using System;
using System.Numerics;
using Raylib_cs;

namespace Client
{
    public class Bacteria : Cell
    {

        // remove that -> health deduction should be in Body class
        private int prevCount = 0;
        private Body body;

        public Bacteria(int screenWidth, int screenHeight, int updateFactor, Color color)
        {
            // set screenHeight
            this.screenWidth = screenWidth;
            this.screenHeight = screenHeight;

            this.updateFactor = updateFactor;

            this.color = color;

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

        public void draw()
        {
            Raylib.DrawCircleV(position, radius, Color.GREEN);
        }



    }
}
