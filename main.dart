import 'package:flutter/material.dart';
import 'package:lottie/lottie.dart';

void main() {
  runApp(
      MaterialApp(
        debugShowCheckedModeBanner: false,
        home: First(),
      )
  );
}
class First extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        backgroundColor: Colors.black,
        appBar: AppBar(
          title: Text('CheerBot😀'),
          centerTitle: true,
          backgroundColor: Colors.black,
        ),
        body: ListView(
          children: [
            LottieBuilder.asset('images/logo.json'
            ,
              height: 400,
              width: 300,
              alignment: Alignment.center,
              fit: BoxFit.fitWidth,
              animate: true,
              repeat: true,
              reverse: true,
              errorBuilder: (BuildContext c,a,s)=>Text('Error occured'),

            ),
          ],
        ),
      ),
    );
  }
}

