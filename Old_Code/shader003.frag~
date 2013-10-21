#version 330
// shader002.frag

// Uniforms:
uniform vec4 light;
uniform vec4 color;

uniform int showLines;

// Interpolated attributes:
in vec4 fragmentNormal;
in vec4 fragmentPosition;
in vec2 fragmentTexCoord;
in vec4 eye;
in vec4 pos;
in float fragmentFocalDistance;

// Output to color frame buffer:
out vec4 outputColor;
  

// Locals

void main()
{
    vec4 lightVector;
    vec4 eyeVector, reflectVector;
    vec4 normalVector;
    vec4 baseColor;
    float ambient, intensity, specular, lambert, s, t;

    ambient = 0.2 ;
    lightVector = normalize(light - fragmentPosition);
    normalVector = normalize(fragmentNormal);
    
    lambert = dot(normalVector, lightVector);
    intensity = max(ambient, lambert);
    baseColor = color;
    if (showLines > 0) {
        s = fragmentTexCoord.s;
        t = fragmentTexCoord.t;
        if (fract(2*s)<0.05) {
            baseColor = vec4(0.0,1.0,0.0,1.0);
        }
        if (fract(2*t)<0.05) {
            baseColor = vec4(0.0,0.0,1.0,1.0);
        }
    }
    outputColor = intensity * baseColor;
    eyeVector = eye;
    if (lambert > 0.0) {
        reflectVector = reflect(-lightVector, normalVector);
        specular = pow(max(dot(reflectVector, eyeVector), 0.0),
                       16);
        specular *= 0.5;
        outputColor += vec4(specular,specular,specular,1.0);
    }
    outputColor.w = 1.0;
    float transparency = 1.0-(fragmentFocalDistance);
    outputColor.w = transparency;
}
