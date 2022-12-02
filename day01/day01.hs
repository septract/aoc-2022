import System.IO (readFile)
import Data.List (lines)
import Data.List (maximumBy)
import Data.Ord (comparing)

-- | Parse a list of numbers in groups and add up the 3 largest sums of the numbers in each group.
--
-- The input is a list of strings, where each string represents a line in the input file.
-- Each line can either be empty (indicating the start of a new group of numbers),
-- or it can contain a number (which will be added to the current group of numbers).
--
-- The output is the sum of the 3 largest sums of the numbers in each group.
parseAndSum :: [String] -> Int
parseAndSum lines = sum $ take 3 $ sortBy (comparing Down) $ map sum groups
  where
    groups = foldr addNumberToGroup [[]] lines

-- | Add a number to the current group of numbers.
--
-- If the number is empty, start a new group of numbers.
-- Otherwise, add the number to the current group of numbers.
addNumberToGroup :: String -> [[Int]] -> [[Int]]
addNumberToGroup line groups
    | null line  = [] : groups
    | otherwise  = (read line : head groups) : tail groups

-- | Read the input from a file and parse it
main :: IO ()
main = do
    -- Read the contents of the file into a string
    input <- readFile "test.txt"

    -- Split the string into a list of lines
    let lines = lines input

    -- Parse the input and compute the sum of the 3 largest sums
    let totalSum = parseAndSum lines

    -- Print the result
    putStrLn $ "The total sum of the 3 largest sums is: " ++ show totalSum