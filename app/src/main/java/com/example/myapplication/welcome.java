package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

import org.w3c.dom.Text;

public class welcome extends AppCompatActivity {
TextView t1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_welcome);
        t1 = (TextView)findViewById(R.id.tx1);
        Intent intent = getIntent();
        Bundle extras = intent.getExtras();
        if(extras!=null){
            String data = extras.getString("key");
            t1.setText("Hello, "+data);
        }
    }
}