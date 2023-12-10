namespace AdventOfCode {
    class ProblemFour : Problem {
        protected override int ProblemNr{ get { return 4; }}
        public ProblemFour(string folderPath) : base(folderPath) {}
        public static string CreateMD5(string input)
        {
            // Use input string to calculate MD5 hash
            byte[] inputBytes = System.Text.Encoding.ASCII.GetBytes(input);
            byte[] hashBytes = System.Security.Cryptography.MD5.HashData(inputBytes);

            return Convert.ToHexString(hashBytes);
        }
        public override string PartOne() {
            int comboNumber = 1;
            string md5 = CreateMD5(input + $"{comboNumber}");
            while (md5[..5] != "00000") {
                comboNumber++;
                md5 = CreateMD5(input + $"{comboNumber}");
            }
            return $"{comboNumber}";
        }
        public override string PartTwo() {
            int comboNumber = 1;
            string md5 = CreateMD5(input + $"{comboNumber}");
            while (md5[..6] != "000000") {
                comboNumber++;
                md5 = CreateMD5(input + $"{comboNumber}");
            }
            return $"{comboNumber}";
        }
    }
}