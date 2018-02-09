from colored import fg, stylize
import os
import pandas as pd
import sys

def collect_data(in_dir="data", verbose=True):
    """
    Function to load questionnaire data into a DataFrame.
    As files are loading, this function will print each
    filepath it tries to load, prefixing and suffixing as
    follows:
    
    📁 [directory recursion]{yellow} \t
    📊 [file loaded successfully]{green} ,
    !{red} [file failed to load] \n
    
    Parameters
    ----------
    in_dir: str, optional
        path to data directory
        
    verbose: Boolean, optional
        print filepaths as loading
        
    Returns
    -------
    data: DataFrame
        pandas frame with question columns and participant rows
    """
    dataFrames = []
    for d in os.listdir(in_dir):
        fp = os.path.join(
            in_dir,
            d
        )
        if os.path.isdir(fp):
            print(
                "📁 {0}".format(
                    stylize(
                        fp,
                        fg('yellow')
                    )
                ),
                end="\t"
            )
            dataFrames.append(
                collect_data(
                    fp
                )
            )
        else:
            try:
                dataFrames.append(
                    pd.read_csv(
                        fp,
                        low_memory=False
                    )
                )
                print(
                    "📊 {0}".format(
                        stylize(
                            fp,
                            fg('green')
                        )
                    ),
                    end=", "
                )
            except:
                print("{0} {1}: {2}".format(
                    stylize(
                        "!",
                        fg('red')
                    ),
                    fp,
                    stylize(
                        sys.exc_info()[0],
                        fg('red')
                    )
                ))
    return(pd.concat(dataFrames))