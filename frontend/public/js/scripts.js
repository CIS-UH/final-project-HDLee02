async function deleteEntity(url) {
    if (confirm('Are you sure?')) {
        try {
            await axios.delete(url);
            location.reload();
        } catch (error) {
            alert('Error deleting entity');
        }
    }
}

async function updateEntity(url, data) {
    try {
        await axios.put(url, data);
        location.reload();
    } catch (error) {
        alert('Error updating entity');
    }
}

async function createEntity(url, data) {
    try {
        await axios.post(url, data);
        location.reload();
    } catch (error) {
        alert('Error creating entity');
    }
}