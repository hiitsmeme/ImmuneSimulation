using System;
using Raylib_cs;

namespace Client
{
    public class Body
    {
        // screen size
        private int screenWidth;
        private int screenHeight;

        // body properties
        public int health { get; set; }
        
        // constructor
        public Body(int screenWidth, int screenHeight)
        {
            this.screenWidth = screenWidth;
            this.screenHeight = screenHeight;
            this.health = 100;
        }

        public bool updateHealth(int factor)
        {
            Console.WriteLine($"UPDATE HEALTH BY {factor}");
            this.health -= factor;
            if (this.health <= 0)
            {
                return false;
            }
            return true;
        }

        public void draw()
        {
            Raylib.DrawRectangle(0, 0, screenWidth, screenHeight, Color.BEIGE);
        }

        public void displayHealth()
        {
            string text = "Health:" +  this.health.ToString();
            Raylib.DrawText(text, 10, 10, 25, Color.BLACK);
        }
    }
}
