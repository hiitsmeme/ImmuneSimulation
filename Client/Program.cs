using System;
using Raylib_cs;
using Client;


Random rnd = new Random();


// set height and width of win
int screenWidth = 800;
int screenHeight = 800;

int framesCounter = 0;

int updateFactor = 1;


// create body instance
Body body = new Body(screenWidth, screenHeight);

// create Macrophae instances
Macrophage macro1 = new Macrophage(screenWidth, screenHeight, updateFactor);

// create Bacteria instance
Bacteria bac1 = new Bacteria(screenWidth, screenHeight, updateFactor, body);


Raylib.InitWindow(screenWidth, screenHeight, "Immune Simulation");

Raylib.SetTargetFPS(30);

// main game loop
while (!Raylib.WindowShouldClose())
{
    // Update vars
    framesCounter++;
    macro1.updatePosition();
    bac1.updatePosition();
    bac1.deductHealth(framesCounter);

    // Draw
    Console.WriteLine(body.health.ToString());
    Raylib.BeginDrawing();
        Raylib.ClearBackground(Color.WHITE);
        body.draw();
        body.displayHealth();

        bac1.draw();
        macro1.draw();

    Raylib.EndDrawing();
}

Raylib.CloseWindow();

return 0;