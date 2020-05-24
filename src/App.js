import React from "react";

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { data: [["Loading..."]] };
  }
  componentDidMount() {
    // Simple GET request using fetch
    fetch("http://127.0.0.1:5000")
      .then((response) => response.json())
      .then((json) => this.setState({ data: json }));
  }
  render() {
    console.log(this.state.data);
    let arr = this.state.data;
    return (
      <div>
        {arr.map((value) => (
          <div style={{ margin: "1em", backgroundColor: "beige" }}>
            {value.map((v) => (
              <div>{v}</div>
            ))}
          </div>
        ))}
      </div>
    );
  }
}
