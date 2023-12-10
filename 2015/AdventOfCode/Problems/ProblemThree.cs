namespace AdventOfCode {
    class ProblemThree : Problem {
        public ProblemThree(string folderPath) : base(folderPath) {}
        protected override int ProblemNr{ get { return 3; }}
        public override string PartOne() {
            Coordinate santa = new (0, 0);
            HashSet<(int, int, int)> houses = new()
            {
                santa.AsTuple()
            };

            foreach (var direction in input) {
                switch (direction)
                {
                    case '>':
                        santa.Move(Direction.Right);
                        break;
                    case '^':
                        santa.Move(Direction.Up);
                        break;
                    case '<':
                        santa.Move(Direction.Left);
                        break;
                    case 'v':
                        santa.Move(Direction.Down);
                        break;
                    default:
                        break;
                }
                houses.Add(santa.AsTuple());
            }

            return $"{houses.Count}";
        }
        public override string PartTwo() {
            Coordinate santa = new (0,0);
            Coordinate roboSanta = new (0,0);
            HashSet<(int, int, int)> houses = new()
            {
                santa.AsTuple(),
                roboSanta.AsTuple()
            };
            var mover = santa;
            foreach (var direction in input) {
                if (mover == santa) {
                    mover = roboSanta;
                } else {
                    mover = santa;
                }
                switch (direction)
                {
                    case '>':
                        mover.Move(Direction.Right);
                        break;
                    case '^':
                        mover.Move(Direction.Up);
                        break;
                    case '<':
                        mover.Move(Direction.Left);
                        break;
                    case 'v':
                        mover.Move(Direction.Down);
                        break;
                    default:
                        break;
                }
                houses.Add(mover.AsTuple());
            }

            return $"{houses.Count}";
        }
    }
}