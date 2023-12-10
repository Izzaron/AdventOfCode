namespace AdventOfCode {
    abstract class Problem {
        abstract protected int ProblemNr {get;}
        protected readonly string input;
        public Problem(string folderPath) {
            string thispath = $"{folderPath}{ProblemNr}.txt";
            input = File.ReadAllText(thispath);
        }

        public abstract string PartOne();
        public abstract string PartTwo();
    }
}