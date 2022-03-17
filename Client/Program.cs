using System;
using Raylib_cs;
using Client;


Random rnd = new Random();


// set height and width of win
int screenWidth = 800;
int screenHeight = 800;

int updateFactor = 1;

// create ball instances
Macrophage macro1 = new Macrophage(screenWidth, screenHeight, updateFactor);
Macrophage macro2 = new Macrophage(screenWidth, screenHeight, updateFactor);
Macrophage macro3 = new Macrophage(screenWidth, screenHeight, updateFactor);
Macrophage macro4 = new Macrophage(screenWidth, screenHeight, updateFactor);


Raylib.InitWindow(screenWidth, screenHeight, "Immune Simulation");

Raylib.SetTargetFPS(30);

// main game loop
while (!Raylib.WindowShouldClose())
{
    // Update
    // update ball position
    macro1.updatePosition();
    macro2.updatePosition();
    macro3.updatePosition();
    macro4.updatePosition();

    // Draw
    Raylib.BeginDrawing();
        Raylib.ClearBackground(Color.WHITE);

        macro1.draw();
        macro2.draw();
        macro3.draw();
        macro4.draw();

    Raylib.EndDrawing();
}

Raylib.CloseWindow();

return 0;