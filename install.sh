sudo apt update -y
sudo apt autoremove -y
clear


echo ""
echo "Check if python3 lang installed or not..."
echo ""
if ! command -v python3 &> /dev/null
    then
        echo "python3 language not installed."
        echo "Installing python3 Language..."
        echo ""
        sudo apt install python3 -y
    else
        echo "Python Already installed."
fi

sleep 1
clear
echo ""
echo "Check if go lang installed or not..."
echo ""
sleep 2

if ! command -v go &> /dev/null

    then
        echo "Go language not installed."
        echo "Installing Go Language..."
        echo ""
        sudo curl -O https://storage.googleapis.com/golang/go1.8.linux-amd64.tar.gz
        sudo tar -xvf go1.8.linux-amd64.tar.gz
        sudo mv go /usr/local
        sudo nano ~/.profile
        export PATH=$PATH:/usr/local/go/bin
        export GOROOT=$HOME/go
        export PATH=$PATH:$GOROOT/bin
        source ~/.profile

    else
        echo "Go already installed."
fi


# Installing Tools 
mkdir Tools
cd Tools
echo ""
echo "Installing amass"
echo ""
sudo apt install amass


echo ""
echo "Installing sublist3r"
echo ""
sudo apt install sublist3r


echo ""
echo "Installing subfinder"
echo ""
sudo apt install subfinder


echo ""
echo "Installing SubBrute"
echo ""
git clone https://github.com/TheRook/subbrute.git


echo ""
echo "Installing Knock"
echo ""
git clone https://github.com/santiko/KnockPy.git