import time
import os
a = """
                                            $$$$$$$$
                                      $$$$$$$$$$$$$$$$$$
                                  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                                $$$$$$$$$$$$$$$$ $      $$$$$$$$$$$$$$$$$$$
                              $$$$$$$$$$$               $$ $$$$$$$$$$$$$$$$$$
                            $$$$$$$$ $$$                    $$$$$$$$$$$$$$$$$
                  $$$$$$$  $$$$$$$                   $$$$$  $$$$$$$$$$$$$$$$$$
              $$$$$$$$$$$$$$$$$$$        $          $$$$$$$  $$$$$$$$$$$$$$$$$
            $$$$$$$$$$$$$$$$$$$$      $$$$$$$       $$$$$$$  $$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$$$$$     $$$$$$$$        $$$$$   $$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$$$$$$      $$$$$$$     $$$        $$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$        $                  $$$$$$$$$$$$$$$$$$ 
        $$$$$$$$$$$$$$$$$$$$$$$$$$                   $      $$$$$$$$$$$$$$$$$$
      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$                      $$$$$$$$$$$$$$$$$$
      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$            $$$$$ $$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$ $$ $$ $  $$$$$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$$$$$$$$   $ $$$$$$$    $$ $$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$$$$   $$$$$$$$      $ $$$$$$$$$$$$$$
              $$$$$$$$$$$$$$$     $$$$$$$$$$    $  $$$$$ $$$$$$$
                    $$$          $$$$ $$$$  $$ $ $$$$$ $$$$$
                                  $$$$ $$$  $   $ $$ $$$$ $$
                                  $$$$$$$     $ $ $$$$$$$$$$$
                                  $$$$$$ $$$  $ $$$$$$$$$$$$
                                    $$$$$$$$$$$$$$$$$$$$$$$
                                      $$$$$$$$$$$$$$$$$$$$$$
                                    $$$$$$$$$$$$$$$$$$$$$ $$$$
                                  $$$$$$$$$$$$$$$$ $$$$$$$$$$$$
                                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""
b = """
                                            $$$$$$$$
                                      $$$$$$$$$$$$$$$$$$
                                  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                                $$$$$$$$$$$$$$$$ $      $$$$$$$$$$$$$$$$$$$
                              $$$$$$$$$$$               $$ $$$$$$$$$$$$$$$$$$
                            $$$$$$$$ $$$                    $$$$$$$$$$$$$$$$$
                        $  $$$$$$$                   $$$$$  $$$$$$$$$$$$$$$$$$
                    $$$$$$$$$$$$$                   $$$$$$$  $$$$$$$$$$$$$$$$$
                  $$$$$$$$$$$$$$    $$$$$$$$        $$$$$$$  $$$$$$$$$$$$$$$$$$
                $$$$$$$$$$$$$$$$     $$$$$$$$        $$$$$   $$$$$$$$$$$$$$$$$$
                $$$$$$$$$$$$$$$$$                             $$$$$$$$$$$$$$$$$$
              $$$$$$$$$$$$$$$$$$$       $$                  $$$$$$$$$$$$$$$$$$ 
              $$$$$$$$$$$$$$$$$$$$         $$$              $$$$$$$$$$$$$$$$$$
            $$$$$$$$$$$$$$$$$$$$$$$          $$$$$$      $$$$$$$$$$$$$$$$$$
            $$$$$$$$$$$$$$$$$$$$$$$$$                  $$$$$$$$$$$$$$$$$$$
              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$
              $$$$$$$$$$$$$$$$$$$$ $$ $$ $  $$$$$$$$$$$$$$$$$$$$$
                $$$$$$$$$$$$$$$$$$$   $ $$$$$$$    $$ $$$$$$$$$$$$
                $$$$$$$$$$$$$$$   $$$$$$$$      $ $$$$$$$$$$$$$$
                    $$$$$$$$$     $$$$$$$$$$    $  $$$$$ $$$$$$$
                          $$$    $$$$ $$$$  $$ $ $$$$$ $$$$$
                                  $$$$ $$$  $   $ $$ $$$$ $$
                                  $$$$$$$     $ $ $$$$$$$$$$$
                                  $$$$$$ $$$  $ $$$$$$$$$$$$
                                    $$$$$$$$$$$$$$$$$$$$$$$
                                      $$$$$$$$$$$$$$$$$$$$$$
                                    $$$$$$$$$$$$$$$$$$$$$ $$$$
                                  $$$$$$$$$$$$$$$$ $$$$$$$$$$$$
                                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""
i = 1
for i in range(4):
  os.system('cls')
  print(a)
  time.sleep(1)
  os.system('cls')
  print(b)
  time.sleep(1)
  i = i+1
