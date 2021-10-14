mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"sriprakhar17@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
mkdir -p ~/.streamlit

echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
