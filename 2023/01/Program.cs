// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

int sumTotal = 0;

Dictionary<string, int> conversions = new Dictionary<string, int>()
{
    {"one", 1},
    {"two", 2},
    {"three", 3},
    {"four", 4},
    {"five", 5},
    {"six", 6},
    {"seven", 7},
    {"eight", 8},
    {"nine", 9},
};

try {
    using (StreamReader sr = new StreamReader("input.txt")) {
        string line;
        while ((line = sr.ReadLine()) != null)
        {
            List<string> possibleWords = new List<string>();

            Console.WriteLine("******");
            Console.WriteLine(line);
            
            int number = 0;
            int firstNum = 0;
            int lastNum = 0;
            bool numSeen = false;
            string currentWord = "";
            foreach (char c in line) {
                bool isNum = int.TryParse(c.ToString(), out number);
                if (isNum) {
                    possibleWords.Clear();
                    if (numSeen)
                        lastNum = number;
                    else {
                        firstNum = number;
                        numSeen = true;
                    }
                }
                else {


                    currentWord += c;
                    Console.WriteLine(currentWord);

                    // possibleWords = possibleWords.ForEach(pw => pw = pw += c);
                    possibleWords = possibleWords.Select(pw => string.Concat(pw, c)).ToList();
                    possibleWords.Add(c.ToString());


                    var matches = conversions.Keys.Intersect(possibleWords);
                    if (matches.Count() > 0) {
                        // number = conversions[currentWord];
                        string numberWord = matches.First();
                        Console.WriteLine($"INTERSECTION: {numberWord}");
                        number = conversions[numberWord];
                        if (numSeen)
                            lastNum = number;
                        else {
                            firstNum = number;
                            numSeen = true;
                        }
                        currentWord = "";
                        possibleWords.Clear();
                    } 
                    // else {
                    //     possibleWords.ForEach(pw => pw = pw += c);
                    //     possibleWords.Add(c.ToString());
                    // }
                }
            }
            if (lastNum == 0)
                lastNum = firstNum;

            Console.WriteLine($"{firstNum} and {lastNum}");
            string concatNums = $"{firstNum}{lastNum}";
            Console.WriteLine(concatNums);
            sumTotal += int.Parse(concatNums);
        }
    }
}
catch (Exception ex) {
    Console.WriteLine(ex.Message);
}

Console.WriteLine($"sum total: {sumTotal}");