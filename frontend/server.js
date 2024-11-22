const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const app = express();

app.set('view engine', 'ejs');
app.set('views', './views');
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));

const API_BASE_URL = 'http://127.0.0.1:5000/api';

// Route to display homepage (redirect to /investors)
app.get('/', (req, res) => {
    res.redirect('/investors');
});

// Route to display investors
app.get('/investors', async (req, res) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/investor`);
        res.render('pages/investors', { investors: response.data });
    } catch (err) {
        res.render('pages/investors', { investors: [], error: err.message });
    }
});

// Route to handle form submissions for adding an investor
app.post('/investors', async (req, res) => {
    try {
        await axios.post(`${API_BASE_URL}/investor`, {
            firstname: req.body.firstname,
            lastname: req.body.lastname,
        });
        res.redirect('/investors');
    } catch (err) {
        res.redirect('/investors');
    }
});

// Route to display stocks
app.get('/stocks', async (req, res) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/stock`);
        res.render('pages/stocks', { stocks: response.data });
    } catch (err) {
        res.render('pages/stocks', { stocks: [], error: err.message });
    }
});

// Route to handle form submissions for adding a stock
app.post('/stocks', async (req, res) => {
    try {
        await axios.post(`${API_BASE_URL}/stock`, {
            stockname: req.body.stockname,
            abbreviation: req.body.abbreviation,
            currentprice: req.body.currentprice,
        });
        res.redirect('/stocks');
    } catch (err) {
        res.redirect('/stocks');
    }
});

// Route to display bonds
app.get('/bonds', async (req, res) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/bond`);
        res.render('pages/bonds', { bonds: response.data });
    } catch (err) {
        res.render('pages/bonds', { bonds: [], error: err.message });
    }
});

// Route to handle form submissions for adding a bond
app.post('/bonds', async (req, res) => {
    try {
        await axios.post(`${API_BASE_URL}/bond`, {
            bondname: req.body.bondname,
            abbreviation: req.body.abbreviation,
            currentprice: req.body.currentprice,
        });
        res.redirect('/bonds');
    } catch (err) {
        res.redirect('/bonds');
    }
});

// Route to display transactions
app.get('/transactions', async (req, res) => {
    try {
        const investorsResponse = await axios.get(`${API_BASE_URL}/investor`);
        const stocksResponse = await axios.get(`${API_BASE_URL}/stock`);
        const bondsResponse = await axios.get(`${API_BASE_URL}/bond`);
        const stockTransactionsResponse = await axios.get(`${API_BASE_URL}/stocktransaction`);
        const bondTransactionsResponse = await axios.get(`${API_BASE_URL}/bondtransaction`);

        res.render('pages/transactions', {
            investors: investorsResponse.data,
            stocks: stocksResponse.data,
            bonds: bondsResponse.data,
            stocktransactions: stockTransactionsResponse.data,
            bondtransactions: bondTransactionsResponse.data,
        });
    } catch (err) {
        res.render('pages/transactions', {
            investors: [],
            stocks: [],
            bonds: [],
            stocktransactions: [],
            bondtransactions: [],
            error: err.message,
        });
    }
});

// Route to handle stock transaction creation
app.post('/stocktransactions', async (req, res) => {
    try {
        await axios.post(`${API_BASE_URL}/stocktransaction`, {
            investorid: req.body.investorid,
            stockid: req.body.stockid,
            quantity: req.body.quantity,
        });
        res.redirect('/transactions');
    } catch (err) {
        res.redirect('/transactions');
    }
});

// Route to handle bond transaction creation
app.post('/bondtransactions', async (req, res) => {
    try {
        await axios.post(`${API_BASE_URL}/bondtransaction`, {
            investorid: req.body.investorid,
            bondid: req.body.bondid,
            quantity: req.body.quantity,
        });
        res.redirect('/transactions');
    } catch (err) {
        res.redirect('/transactions');
    }
});

app.listen(3000, () => {
    console.log('Frontend server is running on http://localhost:3000');
});
