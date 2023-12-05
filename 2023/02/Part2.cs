public static class Part2 {
    public static int Run() {
        int powerSum = 0;

        // using (StreamReader sr = new StreamReader("sample.txt"))
        using (StreamReader sr = new StreamReader("input.txt"))
        {
            string line;
            while ((line = sr.ReadLine()) != null)
            {
                Console.WriteLine(line);

                int id = GetGameID(line);

                ColorCounts gameMax = new ColorCounts() {
                    Red = 0,
                    Blue = 0,
                    Green = 0,
                };

                string[] rounds = GetRounds(line);
                foreach (string r in rounds) {
                    ColorCounts roundCounts = GetColorCounts(r);
                    gameMax = GetMaxPossibleColors(gameMax, roundCounts);
                }

                Console.WriteLine($"game max: {gameMax}");
                int power = gameMax.GetPower();
                Console.WriteLine($"Power: {power}");
                powerSum += power;
            }
        }
        return powerSum;
    }

    private static int GetGameID(string line) {
        string secondTerm = line.Split(" ")[1];
        string numberNotColon = secondTerm.Split(":")[0];
        // char firstCharOfSecondTerm = secondTerm[0];
        return int.Parse(numberNotColon);
    }

    private static string[] GetRounds(string line) {
        string gameInfo = line.Split(":")[1];
        gameInfo = gameInfo.TrimStart(); // get rid of start whitespace
        string[] rounds = gameInfo.Split(";");
        return rounds;
    }

    private static ColorCounts GetColorCounts(string round) {
        round = round.TrimStart();
        ColorCounts cc = new ColorCounts();
        string[] colorPhrases = round.Split(",");
        foreach (string p in colorPhrases) {
            string phrase = p.TrimStart();
            string[] phraseParts = phrase.Split(" ");
            int amt = int.Parse(phraseParts[0]);
            string color = phraseParts[1];

            if (color == "red")
                cc.Red = amt;
            if (color == "blue")
                cc.Blue = amt;
            if (color == "green")
                cc.Green = amt;
        }
        return cc;
    }

    private static ColorCounts GetMaxPossibleColors(ColorCounts c1, ColorCounts c2) {
        return new ColorCounts() {
            Red = Math.Max(c1.Red, c2.Red),
            Blue = Math.Max(c1.Blue, c2.Blue),
            Green = Math.Max(c1.Green, c2.Green),
        };
    }

    // private static ColorCounts GetMinPossibleColors(ColorCounts c1, ColorCounts c2) {
    //     // return new ColorCounts() {
    //     //     Red = Math.Min(c1.Red, c2.Red),
    //     //     Blue = Math.Min(c1.Blue, c2.Blue),
    //     //     Green = Math.Min(c1.Green, c2.Green),
    //     // };

    //     return new ColorCounts() {
    //         Red = LesserOfTwoNullableInts(c1.Red, c2.Red),
    //         Blue = LesserOfTwoNullableInts(c1.Blue, c2.Blue),
    //         Green = LesserOfTwoNullableInts(c1.Green, c2.Green),
    //     };
    // }

    // private static int? LesserOfTwoNullableInts(int? a, int? b) {
    //     return a < b ? a : b ?? a;
    // }

//     public class ColorCounts {
//         public int? Red { get; set; }
//         public int? Blue { get; set; }
//         public int? Green { get; set; }
//         public int GetPower() {
//             if (Red == null && Blue == null && Green == null)
//                 return 0;

//             return Red ?? 1 * Blue ?? 1 * Green ?? 1;
//         }

//         public override string ToString() {
//             return $"r{Red} b{Blue} g{Green}";
//         }
//     }
// }

    public class ColorCounts {
        public int Red { get; set; }
        public int Blue { get; set; }
        public int Green { get; set; }
        public int GetPower() {
            if (Red == 0 && Blue == 0 && Green == 0)
                return 0;

            return Math.Max(Red, 1) * Math.Max(Blue, 1) * Math.Max(Green, 1);
        }

        public override string ToString() {
            return $"r{Red} b{Blue} g{Green}";
        }
    }
}