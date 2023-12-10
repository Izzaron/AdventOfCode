// objectify

// * S - Single responsibility
// * O - Open for extention, close for modification
// L - Liskov: should not have to know if super class or class
// I - Interface segregation: Dont force more interfaces that is used/needed
// * D - Dependency inversion: Depend on abstractions, not concretions

// responsibilities
// 1. read file
// 2. parse file
// 3. "business logic"
// 4. print answer

using AdventOfCode;

char separator = Path.DirectorySeparatorChar;
string folderPath = $".{separator}inputs{separator}";

Problem problem = new ProblemFour(folderPath);

Console.WriteLine(problem.PartOne());
Console.WriteLine(problem.PartTwo());