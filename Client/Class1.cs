using System;
using System.Numerics;
using Raylib_cs;

namespace Client
{
    public class Tracker
    {
        // screen size
        private int screenWidth;
        private int screenHeight;

        private Array[] overlapping;

        public Bacteria[] TrackingBacteria;
        public Macrophage[] TrackingMarcophages;

        // constructor
        public Tracker(int screenWidth, int screenHeight)
        {
            this.screenWidth = screenWidth;
            this.screenHeight = screenHeight;
        }

        public Array[] checkOverlap()
        {
            for (int i = 0; i < TrackingBacteria.Length; i++)
            {
                for (int j = 0; j < TrackingMarcophages.Length; i++)
                {
                    if (TrackingBacteria[i].getPosition() == TrackingMarcophages[j].getPosition())
                    {
                        
                    }
                }
            }
            return overlapping;

        }
    }
}
