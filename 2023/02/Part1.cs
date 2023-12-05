public static class Part1 {
    public static int Run() {
        int idSum = 0;

        ColorCounts bagMax = new ColorCounts()
        {
            Red = 12,
            Green = 13,
            Blue = 14
        };

        // using (StreamReader sr = new StreamReader("sample.txt"))
        using (StreamReader sr = new StreamReader("input.txt"))
        {
            string line;
            while ((line = sr.ReadLine()) != null)
            {
                Console.WriteLine(line);

                int id = GetGameID(line);

                ColorCounts gameMax = new ColorCounts();
                string[] rounds = GetRounds(line);
                foreach (string r in rounds) {
                    ColorCounts roundCounts = GetColorCounts(r);
                    gameMax = GetMaxPossibleColors(gameMax, roundCounts);
                }

                string bagMaxStr = bagMax.ToString();
                string gameMaxStr = gameMax.ToString();
                Console.WriteLine(gameMaxStr);
                string comboMaxStr = GetMaxPossibleColors(bagMax, gameMax).ToString();

                if(comboMaxStr.Equals(bagMaxStr)) {
                    idSum += id;
                }
            }
        }

        
        return idSum;
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

    public class ColorCounts {
        public int Red { get; set; }
        public int Blue { get; set; }
        public int Green { get; set; }

        public override string ToString() {
            return $"r{Red} b{Blue} g{Green}";
        }
    }
}