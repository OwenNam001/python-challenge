## PyBank Challenge

**Objective**: Analyze financial records using a dataset named `budget_data.csv`. The script provides:

- Total number of months included in the dataset.
- Net total amount of "Profit/Losses" over the entire period.
- Average change in "Profit/Losses" over the entire period.
- Greatest increase in profits (date and amount) over the entire period.
- Greatest decrease in profits (date and amount) over the entire period.

The script outputs the analysis to the terminal and exports a text file within the `analysis` folder.

## PyPoll Challenge

**Objective**: Assist a small town to modernize its vote-counting process using a dataset called `election_data.csv`. The script accomplishes:

- Total number of votes cast.
- Complete list of candidates who received votes using dictionay that contains single pair (candidate, votes)
- Percentage of votes each candidate won.
- Total number of votes each candidate won.
- Winner of the election based on popular vote.

Results are displayed in the terminal and saved to a text file in the `analysis` folder.

## Coding Environment
- Python
- VS Code
- Gitlab
- Github


## Repository Structure
```plaintext
python-challenge/
│
├── PyBank/
│   ├── main.py              # Main script for PyBank analysis
│   ├── Resources/
│   │   └── budget_data.csv  # Dataset for analysis
│   └── analysis/
│       └── analysis.txt     # Output text file with the financial analysis results
│
├── PyPoll/
│   ├── main.py              # Main script for PyPoll analysis
│   ├── Resources/
│   │   └── election_data.csv  # Dataset for analysis
│   └── analysis/
│       └── analysis.txt       # Output text file with the election results
│
└── README.md               # Documentation and instructions
