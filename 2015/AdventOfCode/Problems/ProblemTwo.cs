using System.Security.Cryptography;

namespace AdventOfCode {
    class ProblemTwo : Problem {
        protected override int ProblemNr{ get { return 2; }}
        public ProblemTwo(string folderPath) : base(folderPath) {}
        public override string PartOne() {
            return ProblemBody(sides => sides[0]*sides[1]*3 + sides[0]*sides[2]*2 + sides[1]*sides[2]*2);
        }
        public override string PartTwo() {
            return ProblemBody(sides => sides[0]*2 + sides[1]*2 + sides[0]*sides[1]*sides[2]);
        }
        private string ProblemBody(Func<List<int>,int> presentFunction) {

            string[] lines = input.Split('\n');

            int total = 0;

            foreach(string line in lines) {
                List<int> sides = line.Split('x').ToList().ConvertAll(int.Parse);
                sides.Sort();
                total += presentFunction(sides);
            }

            return $"{total}";
        }
    }
}