function fetchData() {
    const reportType = document.getElementById('reportType').value;
    const frequency = document.getElementById('frequency').value;
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;
    

    fetch(`/api/total_miles_driven?report_type=${reportType}&frequency=${frequency}&start_date=${startDate}&end_date=${endDate}`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            const totalMilesDriven = data.total_miles_driven;
            const ctx = document.getElementById('myChart').getContext('2d');
            const result = document.getElementById('dataContainer').innerText=totalMilesDriven;
            const myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Total Miles Driven'],
                    datasets: [{
                        label: 'Total Miles Driven',
                        data: [totalMilesDriven],
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error:', error));
}
var button = document.getElementById('fetchData');

    // Add an onclick event listener to the button
    button.onclick = function() {
        // Your event handling code here
        fetchData();
    };
