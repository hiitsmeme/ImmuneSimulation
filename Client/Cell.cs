using System;
using System.Numerics;
using Raylib_cs;

namespace Client
{
    public class Cell
    {
        // screen size
        protected int screenWidth;
        protected int screenHeight;

        // visualization properties
        protected float posx;
        protected float posy;
        protected int radius = 5;
        protected int updateFactor;
        public Vector2 position;
        protected Color color;

        // constructor
        public Cell(int screenWidth, int screenHeight, int updateFactor, Color color)
        {
            // set screenHeight
            this.screenWidth = screenWidth;
            this.screenHeight = screenHeight;

            this.updateFactor = updateFactor;

            this.color = color;

            posx = (float)screenWidth / 2 + 20;
            posy = (float)screenHeight / 2 + 20;
        }

        //------methods------//

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
            Raylib.DrawCircleV(position, radius, this.color);
        }

    }
}