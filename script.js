document.getElementById('marksForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const studentName = document.getElementById('studentName').value;
    const subject1 = parseInt(document.getElementById('subject1').value);
    const subject2 = parseInt(document.getElementById('subject2').value);
    const totalMarks = subject1 + subject2;
    const percentage = (totalMarks / 200) * 100;

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `Student: <strong>${studentName}</strong><br>
                           Subject 1 Marks: <strong>${subject1}</strong><br>
                           Subject 2 Marks: <strong>${subject2}</strong><br>
                           Total Marks: <strong>${totalMarks}</strong><br>
                           Percentage: <strong>${percentage.toFixed(2)}%</strong>`;
    resultDiv.classList.add('show');
});

document.getElementById('resetButton').addEventListener('click', function() {
    const resultDiv = document.getElementById('result');
    resultDiv.classList.remove('show');
});
