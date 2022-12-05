using System;
using Raylib_cs;
using System.Numerics;

namespace Client
{
    public class Macrophage
    {
        // screen size
        private int screenWidth;
        private int screenHeight;

        // ball properties
        private float posx;
        private float posy;
        private int radius = 10;
        private int updateFactor;
        public Vector2 position;

        // constructor
        public Macrophage(int screenWidth, int screenHeight, int updateFactor)
        {
            // set screenHeight
            this.screenWidth = screenWidth;
            this.screenHeight = screenHeight;

            this.updateFactor = updateFactor;

            posx = (float) screenWidth / 2;
            posy = (float) screenHeight / 2;
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

        public Vector2 getPosition()
        {
            return position;
        }

        public void draw()
        {
            Raylib.DrawCircleV(position, radius, Color.VIOLET);
        }

    }
}
