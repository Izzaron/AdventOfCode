namespace AdventOfCode {
    public class Coordinate {
        int _x;
        int _y;
        int _z;
        public Coordinate(int x, int y, int z = 0) {
            _x = x;
            _y = y;
            _z = z;
        }
        public void Move(Func<(int,int,int),(int,int,int)> translation, int steps = 1) {
            for (int i = 0; i < steps; i++)
            {
                (_x,_y,_z) = translation((_x, _y, _z));
            }
        }
        public (int,int,int) AsTuple() {
            return new (_x,_y,_z);
        }
    }
}