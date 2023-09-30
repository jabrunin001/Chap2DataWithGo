package main

import (
	"fmt"
	"math"

	"github.com/montanaflynn/stats"
)

func main() {
	// Define the original Anscombe Quartet data
	x := []float64{10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5}
	y1 := []float64{8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68}
	y2 := []float64{9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74}
	y3 := []float64{7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73}
	y4 := []float64{6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89}

	// Generate the modified datasets
	y1_new := make([]float64, len(y1))
	y2_new := make([]float64, len(y2))
	y3_new := make([]float64, len(y3))
	y4_new := make([]float64, len(y4))

	avgX, _ := stats.Mean(x) // Corrected mean calculation

	for i := range y1 {
		y1_new[i] = y1[i] + (x[i]-avgX)*2.0
		y2_new[i] = y2[i] + math.Sin(x[i])*2
		y3_new[i] = y3[i] + math.Log(x[i])
		y4_new[i] = y4[i] + math.Exp((x[i]-avgX)/5.0)
	}

	// Compute and print linear regression coefficients for the modified datasets
	printRegressionCoefficients("Quadratic Trend", x, y1_new)
	printRegressionCoefficients("Sinusoidal Pattern", x, y2_new)
	printRegressionCoefficients("Logarithmic Pattern", x, y3_new)
	printRegressionCoefficients("Exponential Increase", x, y4_new)
}

func printRegressionCoefficients(name string, x, y []float64) {
	intercept, slope := linearRegression(x, y)
	fmt.Printf("\nFor the %s dataset:\n", name)
	fmt.Printf("- Intercept: %f\n", intercept)
	fmt.Printf("- Slope: %f\n", slope)
}

func linearRegression(x, y []float64) (intercept, slope float64) {
	n := len(x)
	sumX, _ := stats.Sum(x)
	sumY, _ := stats.Sum(y)
	sumXY := 0.0
	sumX2 := 0.0

	for i := 0; i < n; i++ {
		sumXY += x[i] * y[i]
		sumX2 += x[i] * x[i]
	}

	slope = (float64(n)*sumXY - sumX*sumY) / (float64(n)*sumX2 - sumX*sumX)
	intercept = (sumY - slope*sumX) / float64(n)
	return
}
