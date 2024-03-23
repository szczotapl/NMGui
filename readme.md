<h1>NMGui</h1>

<p>NMGui is a simple graphical user interface for managing network connections using NetworkManager (nm). It provides basic functionalities like viewing available network connections, refreshing the list, connecting to a network, and disconnecting from a network.</p>

<h2>Features</h2>

<ul>
    <li>View a list of available network connections.</li>
    <li>Connect to a network.</li>
    <li>Disconnect from a network.</li>
</ul>

<h2>Requirements</h2>

<ul>
    <li>Python 3</li>
    <li>Gtk+ 3</li>
</ul>

<h2>Installation</h2>
<h3>Automatic (with <a href="https://github.com/riviox/gitman">GitMan</a>)</h3>
<ol>
    <pre><code>gitman -S nmgui</code></pre>
</ol>
<h3>Manual</h3>
<ol>
    <li>Clone the repository:</li>
</ol>

<pre><code>git clone https://github.com/riviox/NMGui.git
</code></pre>

<ol start="2">
    <li>Navigate to the directory:</li>
</ol>

<pre><code>cd NMGui
</code></pre>

<ol start="3">
    <li>Run:</li>
</ol>

<pre><code>make install && nmgui
</code></pre>

<h2>Usage</h2>

<ol>
    <li>Click on the "Refresh" button to update the list of available network connections.</li>
    <li>Select a network from the list.</li>
    <li>Click on the "Connect" button to connect to the selected network.</li>
    <li>To disconnect from a network, select it from the list and click on the "Disconnect" button.</li>
</ol>