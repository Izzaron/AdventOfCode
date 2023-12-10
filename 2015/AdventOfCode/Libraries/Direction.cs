namespace AdventOfCode {
    public abstract class Direction {
        public static (int,int,int) Right((int x,int y,int z) coord) {
            return (coord.x + 1,    coord.y,        coord.z);
        }
        public static (int,int,int) Up((int x,int y,int z) coord) {
            return (coord.x,        coord.y + 1,    coord.z);
        }
        public static (int,int,int) Left((int x,int y,int z) coord) {
            return (coord.x - 1,    coord.y,        coord.z);
        }
        public static (int,int,int) Down((int x,int y,int z) coord) {
            return (coord.x,        coord.y - 1,    coord.z);
        }
    }
}