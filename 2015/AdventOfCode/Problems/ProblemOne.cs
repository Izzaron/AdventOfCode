namespace AdventOfCode {
    class ProblemOne : Problem {
        protected override int ProblemNr{ get { return 1; }}
        public ProblemOne(string folderPath) : base(folderPath) {}
        public override string PartOne() {
            int floor = 0;
            floor += input.Count(x => x == '(');
            floor -= input.Count(x => x == ')');
            return $"{floor}";
        }
        public override string PartTwo() {
            int pos = 0;
            int floor = 0;
            while (floor >= 0) {
                if (input[pos] == '(') {
                    floor++;
                } else if (input[pos] == ')') {
                    floor--;
                }
                pos++;
            }
            return $"{pos}";
        }
    }
}